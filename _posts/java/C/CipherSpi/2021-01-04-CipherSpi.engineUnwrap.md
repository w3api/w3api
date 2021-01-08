---
title: CipherSpi.engineUnwrap()
permalink: Java/CipherSpi/engineUnwrap
date: 2021-01-04
key: JavaJava.C.CipherSpi
category: java
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
* **String wrappedKeyAlgorithm**,  {% include w3api/param_description.html metodo=_data parametro="String wrappedKeyAlgorithm" %}
* **int wrappedKeyType**,  {% include w3api/param_description.html metodo=_data parametro="int wrappedKeyType" %}
* **byte[] wrappedKey**,  {% include w3api/param_description.html metodo=_data parametro="byte[] wrappedKey" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [InvalidKeyException](/Java/InvalidKeyException/)

## Clase Padre
[CipherSpi](/Java/CipherSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CipherSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
