---
title: KeyFactory.translateKey()
permalink: Java/KeyFactory/translateKey
date: 2021-01-04
key: JavaJava.K.KeyFactory
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyFactory.metodos valor="translateKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Key translateKey(Key key) throws InvalidKeyException
~~~

## Parámetros
* **Key key**,  {% include w3api/param_description.html metodo=_data parametro="Key key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/)

## Clase Padre
[KeyFactory](/Java/KeyFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
