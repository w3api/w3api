---
title: VirtualMachine.loadAgentLibrary()
permalink: Java/VirtualMachine-com-sun-tools-attach/loadAgentLibrary
date: 2021-01-11
key: JavaJava.V.VirtualMachine-com-sun-tools-attach
category: java
tags: ['java se', 'com.sun.tools.attach', 'jdk.attach', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-tools-attach.metodos valor="loadAgentLibrary" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void loadAgentLibrary(String agentLibrary) throws AgentLoadException, AgentInitializationException, IOException
public abstract void loadAgentLibrary(String agentLibrary, String options) throws AgentLoadException, AgentInitializationException, IOException
~~~

## Parámetros
* **String agentLibrary**,  {% include w3api/param_description.html metodo=_dato parametro="String agentLibrary" %}
* **String options**,  {% include w3api/param_description.html metodo=_dato parametro="String options" %}

## Excepciones
[AgentInitializationException](/Java/AgentInitializationException/), [IOException](/Java/IOException/), [AgentLoadException](/Java/AgentLoadException/), [AgentInitializationException.returnValue()](/Java/AgentInitializationException.returnValue()/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[VirtualMachine](/Java/VirtualMachine-com-sun-tools-attach/)

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
