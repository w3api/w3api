---
title: ForwardingJavaFileManager.getLocationForModule()
permalink: /Java/ForwardingJavaFileManager/getLocationForModule/
date: 2021-01-11
key: Java.F.ForwardingJavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForwardingJavaFileManager.metodos valor="getLocationForModule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JavaFileManager.Location getLocationForModule(JavaFileManager.Location location, String moduleName) throws IOException
public JavaFileManager.Location getLocationForModule(JavaFileManager.Location location, JavaFileObject fo) throws IOException
~~~

## Parámetros
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}
* **String moduleName**,  {% include w3api/param_description.html metodo=_dato parametro="String moduleName" %}
* **JavaFileObject fo**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileObject fo" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ForwardingJavaFileManager](/Java/ForwardingJavaFileManager/)

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
