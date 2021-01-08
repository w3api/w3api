---
title: GroupLayout.addLayoutComponent()
permalink: Java/GroupLayout/addLayoutComponent
date: 2021-01-04
key: JavaJava.G.GroupLayout
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GroupLayout.metodos valor="addLayoutComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addLayoutComponent(Component component, Object constraints)
public void addLayoutComponent(String name, Component component)
~~~

## Parámetros
* **Component component**,  {% include w3api/param_description.html metodo=_data parametro="Component component" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Object constraints**,  {% include w3api/param_description.html metodo=_data parametro="Object constraints" %}

## Clase Padre
[GroupLayout](/Java/GroupLayout/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GroupLayout.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
