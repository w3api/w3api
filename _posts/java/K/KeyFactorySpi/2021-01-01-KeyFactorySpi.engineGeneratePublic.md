---
title: KeyFactorySpi.engineGeneratePublic()
permalink: /Java/KeyFactorySpi/engineGeneratePublic/
date: 2021-01-11
key: Java.K.KeyFactorySpi
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyFactorySpi.metodos valor="engineGeneratePublic" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract PublicKey engineGeneratePublic(KeySpec keySpec) throws InvalidKeySpecException
~~~

## Parámetros
* **KeySpec keySpec**,  {% include w3api/param_description.html metodo=_dato parametro="KeySpec keySpec" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
