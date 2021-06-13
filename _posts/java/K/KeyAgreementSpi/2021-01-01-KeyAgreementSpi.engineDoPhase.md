---
title: KeyAgreementSpi.engineDoPhase()
permalink: /Java/KeyAgreementSpi/engineDoPhase/
date: 2021-01-11
key: Java.K.KeyAgreementSpi
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyAgreementSpi.metodos valor="engineDoPhase" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract Key engineDoPhase(Key key, boolean lastPhase) throws InvalidKeyException, IllegalStateException
~~~

## Parámetros
* **boolean lastPhase**,  {% include w3api/param_description.html metodo=_dato parametro="boolean lastPhase" %}
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[KeyAgreementSpi](/Java/KeyAgreementSpi/)

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
