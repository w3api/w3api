---
title: VirtualMachine.loadAgent()
permalink: Java/VirtualMachine-com-sun-tools-attach/loadAgent
date: 2021-01-11
key: JavaJava.V.VirtualMachine-com-sun-tools-attach
category: java
tags: ['java se', 'com.sun.tools.attach', 'jdk.attach', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-tools-attach.metodos valor="loadAgent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void loadAgent(String agent) throws AgentLoadException, AgentInitializationException, IOException
public abstract void loadAgent(String agent, String options) throws AgentLoadException, AgentInitializationException, IOException
~~~

## Parámetros
* **String agent**,  {% include w3api/param_description.html metodo=_dato parametro="String agent" %}
* **String options**,  {% include w3api/param_description.html metodo=_dato parametro="String options" %}

## Excepciones
[AgentLoadException](/Java/AgentLoadException/), [AgentInitializationException](/Java/AgentInitializationException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

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
