---
title: DefaultStyledDocument.insert()
permalink: Java/DefaultStyledDocument/insert
date: 2021-01-04
key: JavaJava.D.DefaultStyledDocument
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultStyledDocument.metodos valor="insert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void insert(int offset, DefaultStyledDocument.ElementSpec[] data) throws BadLocationException
~~~

## Parámetros
* **DefaultStyledDocument.ElementSpec[] data**,  {% include w3api/param_description.html metodo=_data parametro="DefaultStyledDocument.ElementSpec[] data" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[DefaultStyledDocument](/Java/DefaultStyledDocument/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultStyledDocument.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
