---
title: CipherSpi.engineUnwrap()
permalink: /Java/CipherSpi/engineUnwrap/
date: 2021-01-11
key: Java.C.CipherSpi
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CipherSpi.metodos valor="engineUnwrap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Key engineUnwrap(byte[] wrappedKey, String wrappedKeyAlgorithm, int wrappedKeyType) throws InvalidKeyException, NoSuchAlgorithmException
~~~

## Parámetros
* **String wrappedKeyAlgorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String wrappedKeyAlgorithm" %}
* **byte[] wrappedKey**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] wrappedKey" %}
* **int wrappedKeyType**,  {% include w3api/param_description.html metodo=_dato parametro="int wrappedKeyType" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [InvalidKeyException](/Java/InvalidKeyException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
