---
title: AttachingConnector.attach()
permalink: Java/AttachingConnector/attach
date: 2021-01-04
key: JavaJava.A.AttachingConnector
category: java
tags: ['java se', 'com.sun.jdi.connect', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachingConnector.metodos valor="attach" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
VirtualMachine attach(Map<String,? extends Connector.Argument> arguments) throws IOException, IllegalConnectorArgumentsException
~~~

## Parámetros
* **? extends Connector.Argument&gt; arguments**,  {% include w3api/param_description.html metodo=_data parametro="? extends Connector.Argument> arguments" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}

## Excepciones
[TransportTimeoutException](/Java/TransportTimeoutException/), [IllegalConnectorArgumentsException](/Java/IllegalConnectorArgumentsException/), [IOException](/Java/IOException/)

## Clase Padre
[AttachingConnector](/Java/AttachingConnector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttachingConnector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
