---
title: ForwardingJavaFileManager.getFileForInput()
permalink: Java/ForwardingJavaFileManager/getFileForInput
date: 2021-01-04
key: JavaJava.F.ForwardingJavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForwardingJavaFileManager.metodos valor="getFileForInput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileObject getFileForInput(JavaFileManager.Location location, String packageName, String relativeName) throws IOException
~~~

## Parámetros
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileManager.Location location" %}
* **String relativeName**,  {% include w3api/param_description.html metodo=_data parametro="String relativeName" %}
* **String packageName**,  {% include w3api/param_description.html metodo=_data parametro="String packageName" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ForwardingJavaFileManager](/Java/ForwardingJavaFileManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForwardingJavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
