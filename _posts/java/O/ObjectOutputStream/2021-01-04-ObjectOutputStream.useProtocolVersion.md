---
title: ObjectOutputStream.useProtocolVersion()
permalink: Java/ObjectOutputStream/useProtocolVersion
date: 2021-01-04
key: JavaJava.O.ObjectOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutputStream.metodos valor="useProtocolVersion" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void useProtocolVersion(int version) throws IOException
~~~

## Parámetros
* **int version**,  {% include w3api/param_description.html metodo=_data parametro="int version" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ObjectOutputStream](/Java/ObjectOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
