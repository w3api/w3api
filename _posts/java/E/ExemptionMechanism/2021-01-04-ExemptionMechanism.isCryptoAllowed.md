---
title: ExemptionMechanism.isCryptoAllowed()
permalink: Java/ExemptionMechanism/isCryptoAllowed
date: 2021-01-04
key: JavaJava.E.ExemptionMechanism
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExemptionMechanism.metodos valor="isCryptoAllowed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean isCryptoAllowed(Key key) throws ExemptionMechanismException
~~~

## Parámetros
* **Key key**,  {% include w3api/param_description.html metodo=_data parametro="Key key" %}

## Excepciones
[ExemptionMechanismException](/Java/ExemptionMechanismException/)

## Clase Padre
[ExemptionMechanism](/Java/ExemptionMechanism/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExemptionMechanism.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
