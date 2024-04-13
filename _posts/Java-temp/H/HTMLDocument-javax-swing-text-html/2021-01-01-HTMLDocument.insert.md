---
title: HTMLDocument.insert()
permalink: /Java/HTMLDocument-javax-swing-text-html/insert/
date: 2021-01-11
key: Java.H.HTMLDocument-javax-swing-text-html
category: Java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLDocument-javax-swing-text-html.metodos valor="insert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void insert(int offset, DefaultStyledDocument.ElementSpec[] data) throws BadLocationException
~~~

## Parámetros
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **DefaultStyledDocument.ElementSpec[] data**,  {% include w3api/param_description.html metodo=_dato parametro="DefaultStyledDocument.ElementSpec[] data" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[HTMLDocument](/Java/HTMLDocument-javax-swing-text-html/)

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
