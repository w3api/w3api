---
title: LaunchingConnector.launch()
permalink: Java/LaunchingConnector/launch
date: 2021-01-04
key: JavaJava.L.LaunchingConnector
category: java
tags: ['java se', 'com.sun.jdi.connect', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LaunchingConnector.metodos valor="launch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
VirtualMachine launch(Map<String,? extends Connector.Argument> arguments) throws IOException, IllegalConnectorArgumentsException, VMStartException
~~~

## Parámetros
* **? extends Connector.Argument&gt; arguments**,  {% include w3api/param_description.html metodo=_data parametro="? extends Connector.Argument> arguments" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}

## Excepciones
[IllegalConnectorArgumentsException](/Java/IllegalConnectorArgumentsException/), [VMStartException](/Java/VMStartException/), [IOException](/Java/IOException/)

## Clase Padre
[LaunchingConnector](/Java/LaunchingConnector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LaunchingConnector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
