---
title: SaslClient.wrap()
permalink: Java/SaslClient/wrap
date: 2021-01-04
key: JavaJava.S.SaslClient
category: java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SaslClient.metodos valor="wrap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
byte[] wrap(byte[] outgoing, int offset, int len) throws SaslException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] outgoing**,  {% include w3api/param_description.html metodo=_data parametro="byte[] outgoing" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[SaslException](/Java/SaslException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[SaslClient](/Java/SaslClient/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SaslClient.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
