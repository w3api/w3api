---
title: JavaFileManager.getLocationForModule()
permalink: /Java/JavaFileManager/getLocationForModule/
date: 2021-01-11
key: Java.J.JavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaFileManager.metodos valor="getLocationForModule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default JavaFileManager.Location getLocationForModule(JavaFileManager.Location location, String moduleName) throws IOException
default JavaFileManager.Location getLocationForModule(JavaFileManager.Location location, JavaFileObject fo) throws IOException
~~~

## Parámetros
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}
* **String moduleName**,  {% include w3api/param_description.html metodo=_dato parametro="String moduleName" %}
* **JavaFileObject fo**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileObject fo" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[JavaFileManager](/Java/JavaFileManager/)

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
