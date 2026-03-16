import { Component, OnInit, signal } from '@angular/core';
import { ApiService } from '../../services/api';
import { ProjectForm } from '../../components/project-form/project-form';

@Component({
  selector: 'app-projects',
  imports: [ProjectForm],
  templateUrl: './projects.html',
  styleUrl: './projects.css',
})
export class ProjectsComponent implements OnInit {

  projects = signal<any[]>([])
  showProjectForm = signal(false)

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.loadProjects();
  }

  loadProjects() {
    this.api.getProjects().subscribe((res: any) => {
      this.projects.set(res);
    })
  }

  toggleProjectForm() {
    this.showProjectForm.set(!this.showProjectForm());
  }

}
