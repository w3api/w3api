---
title: JTextComponent.print()
permalink: Java/JTextComponent/print
date: 2021-01-04
key: JavaJava.J.JTextComponent
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextComponent.metodos valor="print" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean print() throws PrinterException
public boolean print(MessageFormat headerFormat, MessageFormat footerFormat) throws PrinterException
public boolean print(MessageFormat headerFormat, MessageFormat footerFormat, boolean showPrintDialog, PrintService service, PrintRequestAttributeSet attributes, boolean interactive) throws PrinterException
~~~

## Parámetros
* **MessageFormat footerFormat**,  {% include w3api/param_description.html metodo=_data parametro="MessageFormat footerFormat" %}
* **MessageFormat headerFormat**,  {% include w3api/param_description.html metodo=_data parametro="MessageFormat headerFormat" %}
* **PrintRequestAttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="PrintRequestAttributeSet attributes" %}
* **boolean interactive**,  {% include w3api/param_description.html metodo=_data parametro="boolean interactive" %}
* **boolean showPrintDialog**,  {% include w3api/param_description.html metodo=_data parametro="boolean showPrintDialog" %}
* **PrintService service**,  {% include w3api/param_description.html metodo=_data parametro="PrintService service" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [PrinterException](/Java/PrinterException/)

## Clase Padre
[JTextComponent](/Java/JTextComponent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JTextComponent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
