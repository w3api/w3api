---
title: ListeningConnector.accept()
permalink: /Java/ListeningConnector/accept/
date: 2021-01-11
key: Java.L.ListeningConnector
category: Java
tags: ['java se', 'com.sun.jdi.connect', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.ListeningConnector.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
VirtualMachine accept(Map<String,? extends Connector.Argument> arguments) throws IOException, IllegalConnectorArgumentsException
~~~

## Parámetros
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **? extends Connector.Argument&gt; arguments**,  {% include w3api/param_description.html metodo=_dato parametro="? extends Connector.Argument> arguments" %}

## Excepciones
[IllegalConnectorArgumentsException](/Java/IllegalConnectorArgumentsException/), [IOException](/Java/IOException/), [TransportTimeoutException](/Java/TransportTimeoutException/)

## Clase Padre
[ListeningConnector](/Java/ListeningConnector/)

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
