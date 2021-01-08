---
title: JPopupMenu.insert()
permalink: Java/JPopupMenu/insert
date: 2021-01-04
key: JavaJava.J.JPopupMenu
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPopupMenu.metodos valor="insert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insert(Component component, int index)
public void insert(Action a, int index)
~~~

## Parámetros
* **Component component**,  {% include w3api/param_description.html metodo=_data parametro="Component component" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **Action a**,  {% include w3api/param_description.html metodo=_data parametro="Action a" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JPopupMenu](/Java/JPopupMenu/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JPopupMenu.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
