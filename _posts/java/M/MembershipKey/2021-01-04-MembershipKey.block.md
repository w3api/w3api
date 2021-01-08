---
title: MembershipKey.block()
permalink: Java/MembershipKey/block
date: 2021-01-04
key: JavaJava.M.MembershipKey
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MembershipKey.metodos valor="block" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract MembershipKey block(InetAddress source) throws IOException
~~~

## Parámetros
* **InetAddress source**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress source" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MembershipKey](/Java/MembershipKey/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MembershipKey.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
