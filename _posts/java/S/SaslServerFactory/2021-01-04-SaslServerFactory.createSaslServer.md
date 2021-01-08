---
title: SaslServerFactory.createSaslServer()
permalink: Java/SaslServerFactory/createSaslServer
date: 2021-01-04
key: JavaJava.S.SaslServerFactory
category: java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SaslServerFactory.metodos valor="createSaslServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SaslServer createSaslServer(String mechanism, String protocol, String serverName, Map<String,?> props, CallbackHandler cbh) throws SaslException
~~~

## Parámetros
* **String protocol**,  {% include w3api/param_description.html metodo=_data parametro="String protocol" %}
* **String serverName**,  {% include w3api/param_description.html metodo=_data parametro="String serverName" %}
* **String mechanism**,  {% include w3api/param_description.html metodo=_data parametro="String mechanism" %}
* **?&gt; props**,  {% include w3api/param_description.html metodo=_data parametro="?> props" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **CallbackHandler cbh**,  {% include w3api/param_description.html metodo=_data parametro="CallbackHandler cbh" %}

## Excepciones
[SaslException](/Java/SaslException/)

## Clase Padre
[SaslServerFactory](/Java/SaslServerFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SaslServerFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
