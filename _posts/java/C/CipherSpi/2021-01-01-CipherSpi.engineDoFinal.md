---
title: CipherSpi.engineDoFinal()
permalink: Java/CipherSpi/engineDoFinal
date: 2021-01-11
key: JavaJava.C.CipherSpi
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CipherSpi.metodos valor="engineDoFinal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract byte[] engineDoFinal(byte[] input, int inputOffset, int inputLen) throws IllegalBlockSizeException, BadPaddingException
protected abstract int engineDoFinal(byte[] input, int inputOffset, int inputLen, byte[] output, int outputOffset) throws ShortBufferException, IllegalBlockSizeException, BadPaddingException
protected int engineDoFinal(ByteBuffer input, ByteBuffer output) throws ShortBufferException, IllegalBlockSizeException, BadPaddingException
~~~

## Parámetros
* **ByteBuffer output**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer output" %}
* **int inputLen**,  {% include w3api/param_description.html metodo=_dato parametro="int inputLen" %}
* **ByteBuffer input**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer input" %}
* **int outputOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int outputOffset" %}
* **int inputOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int inputOffset" %}
* **byte[] input**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] input" %}
* **byte[] output**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] output" %}

## Excepciones
[ShortBufferException](/Java/ShortBufferException/), [BadPaddingException](/Java/BadPaddingException/), [IllegalBlockSizeException](/Java/IllegalBlockSizeException/), [AEADBadTagException](/Java/AEADBadTagException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CipherSpi](/Java/CipherSpi/)

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
