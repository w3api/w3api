---
title: SecretKeyFactorySpi.engineTranslateKey()
permalink: Java/SecretKeyFactorySpi/engineTranslateKey
date: 2021-01-04
key: JavaJava.S.SecretKeyFactorySpi
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecretKeyFactorySpi.metodos valor="engineTranslateKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract SecretKey engineTranslateKey(SecretKey key) throws InvalidKeyException
~~~

## Parámetros
* **SecretKey key**,  {% include w3api/param_description.html metodo=_data parametro="SecretKey key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/)

## Clase Padre
[SecretKeyFactorySpi](/Java/SecretKeyFactorySpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecretKeyFactorySpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
