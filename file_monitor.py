import argparse
import sys
import file_monitor2
import db
import notifier

arg_parser = None


def run(args):
    if args['routine_scan']:
        file_monitor2.start_scan(False)
    elif args['silent_scan']:
        file_monitor2.start_scan(True)
    elif args['process_email_queue']:
        notifier.send_queued_messages()
    elif args["export_db"]:
        export_path = input("Enter the output path: ")
        file_monitor2.export_file_records_to_csv(export_path)
    elif args["reset"]:
        ans = input("WARNING: This will delete all database records. Do you really want to continue [Y/N]? ")
        if ans.upper() == "Y":
            db.delete_all_data()
            print("Database has been cleared.")
        else:
            sys.exit()
    else:
        arg_parser.print_help()
        sys.exit()


def generate_argparser():
    ascii_logo = """
 
                                               SIMPLE FILE ACTIVITY MONITORING TOOL
    
    Instructions
    - modify the watch_list.txt and add the path of the directory or file to be watched
    
    Single file format - /home/tarus/Desktop/example.txt
    Directory format - directory path, include subdirectories[true or false], exclude file extensions e.g .css|.xlsx
                     - /home/tarus/Desktop, true, .xlsx

    """
    ap = argparse.ArgumentParser(ascii_logo)

    ap.add_argument("-s", "--silent-scan", action='store_true',
                    help="Use this option whenever you add new files into the directories being watched without getting emails or logs"
                          "It will create records of the files within the directory and save it in the database")

    ap.add_argument("-r", "--routine-scan", action='store_true',
                    help="This scan will generate logs of changes that occur."
                         "This will scan and report the changes that occurs within the directories or files being watched")


    ap.add_argument("-e", "--process-email-queue", action='store_true',
                    help="This scan will send email reports. It is executed by crontabs")

    ap.add_argument("--export-db", action='store_true',
                    help="Export the database file records to a CSV file.")

    ap.add_argument("--reset", action='store_true',
                    help="Empty the file records database. Use this after getting email reports to avoid sending multiple emails of the same file changes")


    return ap


def main():
    global arg_parser
    arg_parser = generate_argparser()

    args = vars(arg_parser.parse_args())
    run(args)


if __name__ == "__main__":
    main()