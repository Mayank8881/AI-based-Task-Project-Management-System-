import { Component, signal } from '@angular/core';
import { ApiService } from '../../services/api';

@Component({
  selector: 'app-project-form',
  imports: [],
  templateUrl: './project-form.html',
  styleUrl: './project-form.css',
})
export class ProjectForm {
  name=signal('')
  description=signal('')
  createdBy=signal('')

  constructor(private api: ApiService) {}

  createProject(){
    if(!this.name || !this.createdBy) {
      alert("Project name and creator required");
      return;
    }

    const payload = {
      name: this.name(),
      description: this.description(),
      created_by: this.createdBy()
    };

    this.api.createProject(payload).subscribe(() => {

      alert("Project created");

      this.name.set('');
      this.description.set('');
      this.createdBy.set('');

    });
  }
}
