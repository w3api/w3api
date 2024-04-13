---
title: CipherSpi.engineWrap()
permalink: /Java/CipherSpi/engineWrap/
date: 2021-01-11
key: Java.C.CipherSpi
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CipherSpi.metodos valor="engineWrap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected byte[] engineWrap(Key key) throws IllegalBlockSizeException, InvalidKeyException
~~~

## Parámetros
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}

## Excepciones
[IllegalBlockSizeException](/Java/IllegalBlockSizeException/), [InvalidKeyException](/Java/InvalidKeyException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[CipherSpi](/Java/CipherSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
