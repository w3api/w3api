---
title: KeyFactorySpi.engineGeneratePrivate()
permalink: Java/KeyFactorySpi/engineGeneratePrivate
date: 2021-01-04
key: JavaJava.K.KeyFactorySpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyFactorySpi.metodos valor="engineGeneratePrivate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract PrivateKey engineGeneratePrivate(KeySpec keySpec) throws InvalidKeySpecException
~~~

## Parámetros
* **KeySpec keySpec**,  {% include w3api/param_description.html metodo=_data parametro="KeySpec keySpec" %}

## Excepciones
[InvalidKeySpecException](/Java/InvalidKeySpecException/)

## Clase Padre
[KeyFactorySpi](/Java/KeyFactorySpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyFactorySpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
