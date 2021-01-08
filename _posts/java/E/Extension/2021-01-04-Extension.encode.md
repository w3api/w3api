---
title: Extension.encode()
permalink: Java/Extension/encode
date: 2021-01-04
key: JavaJava.E.Extension
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Extension.metodos valor="encode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void encode(OutputStream out) throws IOException
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[Extension](/Java/Extension/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.Extension.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
