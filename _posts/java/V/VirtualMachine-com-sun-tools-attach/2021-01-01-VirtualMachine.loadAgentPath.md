---
title: VirtualMachine.loadAgentPath()
permalink: /Java/VirtualMachine-com-sun-tools-attach/loadAgentPath/
date: 2021-01-11
key: Java.V.VirtualMachine-com-sun-tools-attach
category: Java
tags: ['java se', 'com.sun.tools.attach', 'jdk.attach', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-tools-attach.metodos valor="loadAgentPath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void loadAgentPath(String agentPath) throws AgentLoadException, AgentInitializationException, IOException
public abstract void loadAgentPath(String agentPath, String options) throws AgentLoadException, AgentInitializationException, IOException
~~~

## Parámetros
* **String agentPath**,  {% include w3api/param_description.html metodo=_dato parametro="String agentPath" %}
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
