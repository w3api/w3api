---
title: JdiInitiator.JdiInitiator()
permalink: Java/JdiInitiator/JdiInitiator
date: 2021-01-11
key: JavaJava.J.JdiInitiator
category: java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JdiInitiator.constructores valor="JdiInitiator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JdiInitiator(int port, List<String> remoteVMOptions, String remoteAgent, boolean isLaunch, String host, int timeout, Map<String,String> customConnectorArgs)
~~~

## Parámetros
* **int timeout**,  {% include w3api/param_description.html metodo=_dato parametro="int timeout" %}
* **List&lt;String&gt; remoteVMOptions**,  {% include w3api/param_description.html metodo=_dato parametro="List<String> remoteVMOptions" %}
* **String&gt; customConnectorArgs**,  {% include w3api/param_description.html metodo=_dato parametro="String> customConnectorArgs" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}
* **boolean isLaunch**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isLaunch" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **String remoteAgent**,  {% include w3api/param_description.html metodo=_dato parametro="String remoteAgent" %}

## Clase Padre
[JdiInitiator](/Java/JdiInitiator/)

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
