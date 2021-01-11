---
title: KeyFactorySpi.engineTranslateKey()
permalink: Java/KeyFactorySpi/engineTranslateKey
date: 2021-01-11
key: JavaJava.K.KeyFactorySpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyFactorySpi.metodos valor="engineTranslateKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract Key engineTranslateKey(Key key) throws InvalidKeyException
~~~

## Parámetros
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/)

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
