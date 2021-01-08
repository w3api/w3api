---
title: SaslClientFactory.createSaslClient()
permalink: Java/SaslClientFactory/createSaslClient
date: 2021-01-04
key: JavaJava.S.SaslClientFactory
category: java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SaslClientFactory.metodos valor="createSaslClient" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SaslClient createSaslClient(String[] mechanisms, String authorizationId, String protocol, String serverName, Map<String,?> props, CallbackHandler cbh) throws SaslException
~~~

## Parámetros
* **String[] mechanisms**,  {% include w3api/param_description.html metodo=_data parametro="String[] mechanisms" %}
* **String protocol**,  {% include w3api/param_description.html metodo=_data parametro="String protocol" %}
* **String serverName**,  {% include w3api/param_description.html metodo=_data parametro="String serverName" %}
* **?&gt; props**,  {% include w3api/param_description.html metodo=_data parametro="?> props" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **String authorizationId**,  {% include w3api/param_description.html metodo=_data parametro="String authorizationId" %}
* **CallbackHandler cbh**,  {% include w3api/param_description.html metodo=_data parametro="CallbackHandler cbh" %}

## Excepciones
[SaslException](/Java/SaslException/)

## Clase Padre
[SaslClientFactory](/Java/SaslClientFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SaslClientFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
