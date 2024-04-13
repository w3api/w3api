---
title: GroupLayout.addLayoutComponent()
permalink: /Java/GroupLayout/addLayoutComponent/
date: 2021-01-11
key: Java.G.GroupLayout
category: Java
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
* **Object constraints**,  {% include w3api/param_description.html metodo=_dato parametro="Object constraints" %}
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Component component**,  {% include w3api/param_description.html metodo=_dato parametro="Component component" %}

## Clase Padre
[GroupLayout](/Java/GroupLayout/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
