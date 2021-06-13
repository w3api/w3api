---
title: JEditorPane.registerEditorKitForContentType()
permalink: /Java/JEditorPane/registerEditorKitForContentType/
date: 2021-01-11
key: Java.J.JEditorPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JEditorPane.metodos valor="registerEditorKitForContentType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void registerEditorKitForContentType(String type, String classname)
public static void registerEditorKitForContentType(String type, String classname, ClassLoader loader)
~~~

## Parámetros
* **String classname**,  {% include w3api/param_description.html metodo=_dato parametro="String classname" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}

## Clase Padre
[JEditorPane](/Java/JEditorPane/)

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
