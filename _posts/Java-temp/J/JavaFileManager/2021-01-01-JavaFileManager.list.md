---
title: JavaFileManager.list()
permalink: /Java/JavaFileManager/list/
date: 2021-01-11
key: Java.J.JavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaFileManager.metodos valor="list" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Iterable<JavaFileObject> list(JavaFileManager.Location location, String packageName, Set<JavaFileObject.Kind> kinds, boolean recurse) throws IOException
~~~

## Parámetros
* **boolean recurse**,  {% include w3api/param_description.html metodo=_dato parametro="boolean recurse" %}
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}
* **String packageName**,  {% include w3api/param_description.html metodo=_dato parametro="String packageName" %}
* **Set&lt;JavaFileObject.Kind&gt; kinds**,  {% include w3api/param_description.html metodo=_dato parametro="Set<JavaFileObject.Kind> kinds" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

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
