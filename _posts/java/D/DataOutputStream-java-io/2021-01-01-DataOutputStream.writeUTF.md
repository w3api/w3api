---
title: DataOutputStream.writeUTF()
permalink: Java/DataOutputStream-java-io/writeUTF
date: 2021-01-11
key: JavaJava.D.DataOutputStream-java-io
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataOutputStream-java-io.metodos valor="writeUTF" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void writeUTF(String str) throws IOException
~~~

## Parámetros
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[DataOutputStream](/Java/DataOutputStream-java-io/)

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
