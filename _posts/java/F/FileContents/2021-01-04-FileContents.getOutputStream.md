---
title: FileContents.getOutputStream()
permalink: Java/FileContents/getOutputStream
date: 2021-01-04
key: JavaJava.F.FileContents
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileContents.metodos valor="getOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
OutputStream getOutputStream(boolean overwrite) throws IOException
~~~

## Parámetros
* **boolean overwrite**,  {% include w3api/param_description.html metodo=_data parametro="boolean overwrite" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[FileContents](/Java/FileContents/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileContents.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
