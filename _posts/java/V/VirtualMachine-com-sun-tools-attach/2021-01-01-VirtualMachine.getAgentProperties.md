---
title: VirtualMachine.getAgentProperties()
permalink: Java/VirtualMachine-com-sun-tools-attach/getAgentProperties
date: 2021-01-11
key: JavaJava.V.VirtualMachine-com-sun-tools-attach
category: java
tags: ['java se', 'com.sun.tools.attach', 'jdk.attach', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-tools-attach.metodos valor="getAgentProperties" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Properties getAgentProperties() throws IOException
~~~

## Excepciones
[IOException](/Java/IOException/), [AttachOperationFailedException](/Java/AttachOperationFailedException/)

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
