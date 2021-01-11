---
title: SaslClient.getNegotiatedProperty()
permalink: Java/SaslClient/getNegotiatedProperty
date: 2021-01-11
key: JavaJava.S.SaslClient
category: java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SaslClient.metodos valor="getNegotiatedProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getNegotiatedProperty(String propName)
~~~

## Parámetros
* **String propName**,  {% include w3api/param_description.html metodo=_dato parametro="String propName" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[SaslClient](/Java/SaslClient/)

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
