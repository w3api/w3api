---
title: Signature.initSign()
permalink: /Java/Signature/initSign/
date: 2021-01-11
key: Java.S.Signature
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Signature.metodos valor="initSign" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void initSign(PrivateKey privateKey) throws InvalidKeyException
public final void initSign(PrivateKey privateKey, SecureRandom random) throws InvalidKeyException
~~~

## Parámetros
* **PrivateKey privateKey**,  {% include w3api/param_description.html metodo=_dato parametro="PrivateKey privateKey" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/)

## Clase Padre
[Signature](/Java/Signature/)

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
