---
title: ResponseAPDU.ResponseAPDU()
permalink: Java/ResponseAPDU/ResponseAPDU
date: 2021-01-04
key: JavaJava.R.ResponseAPDU
category: java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResponseAPDU.constructores valor="ResponseAPDU" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ResponseAPDU(byte[] apdu)
~~~

## Parámetros
* **byte[] apdu**,  {% include w3api/param_description.html metodo=_data parametro="byte[] apdu" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ResponseAPDU](/Java/ResponseAPDU/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResponseAPDU.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
