---
title: JEditorPane.getStream()
permalink: Java/JEditorPane/getStream
date: 2021-01-04
key: JavaJava.J.JEditorPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JEditorPane.metodos valor="getStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected InputStream getStream(URL page) throws IOException
~~~

## Parámetros
* **URL page**,  {% include w3api/param_description.html metodo=_data parametro="URL page" %}

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
