---
title: KeyAgreement.init()
permalink: /Java/KeyAgreement/init/
date: 2021-01-11
key: Java.K.KeyAgreement
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyAgreement.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void init(Key key) throws InvalidKeyException
public final void init(Key key, SecureRandom random) throws InvalidKeyException
public final void init(Key key, AlgorithmParameterSpec params) throws InvalidKeyException, InvalidAlgorithmParameterException
public final void init(Key key, AlgorithmParameterSpec params, SecureRandom random) throws InvalidKeyException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec params" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[KeyAgreement](/Java/KeyAgreement/)

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
