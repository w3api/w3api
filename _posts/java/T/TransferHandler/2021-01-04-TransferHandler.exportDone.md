---
title: TransferHandler.exportDone()
permalink: Java/TransferHandler/exportDone
date: 2021-01-04
key: JavaJava.T.TransferHandler
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransferHandler.metodos valor="exportDone" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void exportDone(JComponent source, Transferable data, int action)
~~~

## Parámetros
* **int action**,  {% include w3api/param_description.html metodo=_data parametro="int action" %}
* **JComponent source**,  {% include w3api/param_description.html metodo=_data parametro="JComponent source" %}
* **Transferable data**,  {% include w3api/param_description.html metodo=_data parametro="Transferable data" %}

## Clase Padre
[TransferHandler](/Java/TransferHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransferHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
