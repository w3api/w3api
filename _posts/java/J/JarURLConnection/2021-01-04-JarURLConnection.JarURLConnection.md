---
title: JarURLConnection.JarURLConnection()
permalink: Java/JarURLConnection/JarURLConnection
date: 2021-01-04
key: JavaJava.J.JarURLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarURLConnection.constructores valor="JarURLConnection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected JarURLConnection(URL url) throws MalformedURLException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}

## Excepciones
[MalformedURLException](/Java/MalformedURLException/)

## Clase Padre
[JarURLConnection](/Java/JarURLConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JarURLConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
