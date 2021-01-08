---
title: GroupLayout.createParallelGroup()
permalink: Java/GroupLayout/createParallelGroup
date: 2021-01-04
key: JavaJava.G.GroupLayout
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GroupLayout.metodos valor="createParallelGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GroupLayout.ParallelGroup createParallelGroup()
public GroupLayout.ParallelGroup createParallelGroup(GroupLayout.Alignment alignment)
public GroupLayout.ParallelGroup createParallelGroup(GroupLayout.Alignment alignment, boolean resizable)
~~~

## Parámetros
* **GroupLayout.Alignment alignment**,  {% include w3api/param_description.html metodo=_data parametro="GroupLayout.Alignment alignment" %}
* **boolean resizable**,  {% include w3api/param_description.html metodo=_data parametro="boolean resizable" %}

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
{%- for _ldc in site.data.Java.G.GroupLayout.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
