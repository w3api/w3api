---
title: KeyAgreement.doPhase()
permalink: Java/KeyAgreement/doPhase
date: 2021-01-11
key: JavaJava.K.KeyAgreement
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyAgreement.metodos valor="doPhase" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Key doPhase(Key key, boolean lastPhase) throws InvalidKeyException, IllegalStateException
~~~

## Parámetros
* **boolean lastPhase**,  {% include w3api/param_description.html metodo=_dato parametro="boolean lastPhase" %}
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [IllegalStateException](/Java/IllegalStateException/)

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
