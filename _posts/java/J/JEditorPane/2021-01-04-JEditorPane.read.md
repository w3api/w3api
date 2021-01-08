---
title: JEditorPane.read()
permalink: Java/JEditorPane/read
date: 2021-01-04
key: JavaJava.J.JEditorPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JEditorPane.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void read(InputStream in, Object desc) throws IOException
~~~

## Parámetros
* **Object desc**,  {% include w3api/param_description.html metodo=_data parametro="Object desc" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[JEditorPane](/Java/JEditorPane/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JEditorPane.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
