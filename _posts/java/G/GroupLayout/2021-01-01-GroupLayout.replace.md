---
title: GroupLayout.replace()
permalink: Java/GroupLayout/replace
date: 2021-01-11
key: JavaJava.G.GroupLayout
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GroupLayout.metodos valor="replace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void replace(Component existingComponent, Component newComponent)
~~~

## Parámetros
* **Component newComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component newComponent" %}
* **Component existingComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component existingComponent" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
