---
title: JScrollPane.JScrollPane()
permalink: /Java/JScrollPane/JScrollPane/
date: 2021-01-11
key: Java.J.JScrollPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JScrollPane.constructores valor="JScrollPane" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JScrollPane()
public JScrollPane(int vsbPolicy, int hsbPolicy)
public JScrollPane(Component view)
public JScrollPane(Component view, int vsbPolicy, int hsbPolicy)
~~~

## Parámetros
* **int hsbPolicy**,  {% include w3api/param_description.html metodo=_dato parametro="int hsbPolicy" %}
* **int vsbPolicy**,  {% include w3api/param_description.html metodo=_dato parametro="int vsbPolicy" %}
* **Component view**,  {% include w3api/param_description.html metodo=_dato parametro="Component view" %}

## Clase Padre
[JScrollPane](/Java/JScrollPane/)

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
