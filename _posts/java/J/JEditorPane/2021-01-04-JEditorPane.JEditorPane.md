---
title: JEditorPane.JEditorPane()
permalink: Java/JEditorPane/JEditorPane
date: 2021-01-04
key: JavaJava.J.JEditorPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JEditorPane.constructores valor="JEditorPane" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JEditorPane()
public JEditorPane(String url) throws IOException
public JEditorPane(String type, String text)
public JEditorPane(URL initialPage) throws IOException
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **URL initialPage**,  {% include w3api/param_description.html metodo=_data parametro="URL initialPage" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **String url**,  {% include w3api/param_description.html metodo=_data parametro="String url" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

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
